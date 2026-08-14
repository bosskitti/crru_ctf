"""
Fix the cross-lesson conflict: when showSandboxItem runs querySelectorAll('.w-sand-panel'),
it affects ALL lessons on the page. Fix by scoping each lesson's sandbox with a unique
container ID so the JS only affects its own panels.
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db

    # For each lesson 177-180, add a unique wrapper ID and scope the JS
    lesson_configs = {
        177: {'wrapper_id': 'sandbox-177', 'items': ['httpget', 'httppost']},
        178: {'wrapper_id': 'sandbox-178', 'items': ['dirb', 'curl']},
        179: {'wrapper_id': 'sandbox-179', 'items': ['sqlitest', 'cmdtest']},
        180: {'wrapper_id': 'sandbox-180', 'items': ['wpscan', 'joomscan']},
    }

    for lid, config in lesson_configs.items():
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"[!] Lesson {lid} not found")
            continue

        blocks = json.loads(lesson.content)
        val = blocks[1].get('value', '')
        wrapper_id = config['wrapper_id']

        # 1. Wrap the main sandbox div with a unique ID container
        val = val.replace(
            '<div class="w-sandbox-main">',
            f'<div id="{wrapper_id}" class="w-sandbox-main">'
        )

        # 2. Replace the script to use scoped selectors
        # Remove old script
        val = re.sub(r'<script>.*?</script>', '', val, flags=re.DOTALL)

        # Build scoped script
        items = config['items']
        sim_cases = ''
        for item in items:
            sim_cases += f"    // case for {item} handled by startPostSim\n"

        new_script = f'''<script>
window.showSandboxItem = function(itemKey, element) {{
  var container = document.getElementById('{wrapper_id}');
  if (!container) return;
  var items = container.querySelectorAll('.w-nav-item');
  items.forEach(function(i) {{ i.classList.remove('active'); }});
  element.classList.add('active');
  var panels = container.querySelectorAll('.w-sand-panel');
  panels.forEach(function(p) {{ p.classList.remove('active'); }});
  var targetPanel = document.getElementById('panel-' + itemKey);
  if (targetPanel) {{ targetPanel.classList.add('active'); }}
}}
window.startPostSim = function(itemKey) {{
  var term = document.getElementById('term-' + itemKey);
  if (!term) return;
  term.innerHTML = '<span class="prompt">kali$</span> <span class="cmd">Executing...</span>\\n[.] Running command...';
  setTimeout(function() {{
'''
        # Add simulation responses based on lesson
        if lid == 177:
            new_script += '''    if (itemKey === 'httpget') {
      term.innerHTML = '<span class="prompt">client$</span> <span style="color:#3ddc84; font-weight:bold;">HTTP/1.1 200 OK</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Type: text/html\\nContent-Length: 1042\\n\\n&lt;html&gt;&lt;body&gt;&lt;h1&gt;Welcome to RPCA Cyber Club&lt;/h1&gt;&lt;/body&gt;&lt;/html&gt;';
    } else if (itemKey === 'httppost') {
      term.innerHTML = '<span class="prompt">client$</span> <span style="color:#fbbf24; font-weight:bold;">HTTP/1.1 302 Found</span>\\nServer: Apache/2.4.41 (Ubuntu)\\nLocation: /dashboard.php\\nSet-Cookie: session_id=abc123xyz; Path=/; HttpOnly\\n\\n[+] Redirecting to dashboard...';
    }
'''
        elif lid == 178:
            new_script += '''    if (itemKey === 'dirb') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">DIRB scan results:</span>\\nFOUND: http://ctf.rpca.ac.th/backup.zip (CODE: 200)\\nFOUND: http://ctf.rpca.ac.th/old_site.bak (CODE: 200)\\n\\n[+] Dirb completed successfully!';
    } else if (itemKey === 'curl') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#a855f7; font-weight:bold;">HTTP/1.1 200 OK</span>\\nAllow: GET, POST, OPTIONS, TRACE, WebDAV\\nServer: Apache/2.4.41 (Ubuntu)\\nContent-Length: 0\\n\\n[+] OPTIONS check finished.';
    }
'''
        elif lid == 179:
            new_script += '''    if (itemKey === 'sqlitest') {
      term.innerHTML = '<span class="prompt">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\\n\\n[+] Data exfiltration successful!';
    } else if (itemKey === 'cmdtest') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\\nroot:x:0:0:root:/root:/bin/bash\\nbin:x:1:1:bin:/bin:/sbin/nologin\\n\\n[+] Command completed without spaces.';
    }
'''
        elif lid == 180:
            new_script += '''    if (itemKey === 'wpscan') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\\nWordPress version: 6.2.2 (Outdated)\\nFOUND User: admin (ID: 1)\\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\\n\\n[+] WPScan Completed!';
    } else if (itemKey === 'joomscan') {
      term.innerHTML = '<span class="prompt">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\\nJoomla! version: 3.9.22 (Outdated)\\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\\n\\n[+] JoomScan completed successfully.';
    }
'''

        new_script += f'''  }}, 1000);
}}
setTimeout(function() {{
  var container = document.getElementById('{wrapper_id}');
  if (container) {{
    var activeBtn = container.querySelector('.w-nav-item.active');
    if (activeBtn) {{ activeBtn.click(); }}
  }}
}}, 100);
</script>'''

        val = val + new_script
        blocks[1]['value'] = val
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print(f"[OK] Lesson {lid}: scoped sandbox with id='{wrapper_id}'")

    print("\n[DONE] All sandboxes now scoped! No more cross-lesson conflicts.")
