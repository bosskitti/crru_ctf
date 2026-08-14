"""
Fix Lesson 179 & 180 sandbox blocks:
- Add IDs to Run Simulation buttons
- Replace old showSandboxItem/startWebSim global functions with event delegation
"""
import json, re, sys
sys.path.insert(0, '/opt/CTFd')
from CTFd import create_app

app = create_app()

# ── New script for Lesson 179 (SQLi & Command Injection) ──
SCRIPT_179 = """
(function() {
  var startWebSim = function(itemKey) {
    var term = document.getElementById('term-' + itemKey);
    if (!term) return;
    term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Executing commands...</span>\\n[.] Verifying backend sanitization checks...';
    setTimeout(function() {
      if (itemKey === 'sqlitest') {
        term.innerHTML = '<span style="color:#64748b;">db-cli$</span> <span style="color:#3ddc84; font-weight:bold;">UNION select output:</span>\\nID: null | User: admin | Pass: <span style="color:#ef4444;">$2y$10$xyzPasswordHash...</span>\\nID: null | User: user1 | Pass: <span style="color:#ef4444;">$2y$10$abcHashUser1...</span>\\n\\n[+] Data exfiltration successful!';
      } else if (itemKey === 'cmdtest') {
        term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">cat /etc/passwd:</span>\\nroot:x:0:0:root:/root:/bin/bash\\nbin:x:1:1:bin:/bin:/sbin/nologin\\n\\n[+] Command completed without spaces.';
      }
    }, 1000);
  };

  document.addEventListener('click', function(e) {
    var tabSqli = e.target.closest('#nav-item-sqlitest');
    if (tabSqli) {
      var tabCmd = document.getElementById('nav-item-cmdtest');
      var panelSqli = document.getElementById('panel-sqlitest');
      var panelCmd = document.getElementById('panel-cmdtest');
      if (panelSqli && panelCmd) {
        panelSqli.style.display = 'block';
        panelCmd.style.display = 'none';
        tabSqli.classList.add('active');
        if (tabCmd) tabCmd.classList.remove('active');
      }
      return;
    }

    var tabCmd = e.target.closest('#nav-item-cmdtest');
    if (tabCmd) {
      var tabSqli2 = document.getElementById('nav-item-sqlitest');
      var panelSqli2 = document.getElementById('panel-sqlitest');
      var panelCmd2 = document.getElementById('panel-cmdtest');
      if (panelSqli2 && panelCmd2) {
        panelSqli2.style.display = 'none';
        panelCmd2.style.display = 'block';
        tabCmd.classList.add('active');
        if (tabSqli2) tabSqli2.classList.remove('active');
      }
      return;
    }

    var runSqli = e.target.closest('#btn-run-sqlitest');
    if (runSqli) {
      startWebSim('sqlitest');
      return;
    }

    var runCmd = e.target.closest('#btn-run-cmdtest');
    if (runCmd) {
      startWebSim('cmdtest');
      return;
    }
  });
})();
"""

# ── New script for Lesson 180 (CMS Security Audit) ──
SCRIPT_180 = """
(function() {
  var startWebSim = function(itemKey) {
    var term = document.getElementById('term-' + itemKey);
    if (!term) return;
    term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#ffffff; font-weight:bold;">Running CMS mapping audits...</span>\\n[.] Executing target scanner engines...';
    setTimeout(function() {
      if (itemKey === 'wpscan') {
        term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">WPScan Output:</span>\\nWordPress version: 6.2.2 (Outdated)\\nFOUND User: admin (ID: 1)\\nFOUND Vulnerable Plugin: contact-form-7 v5.7.1 (XSS vulnerable)\\n\\n[+] WPScan Completed!';
      } else if (itemKey === 'joomscan') {
        term.innerHTML = '<span style="color:#64748b;">kali$</span> <span style="color:#3ddc84; font-weight:bold;">OWASP Joomla! Vulnerability Scanner:</span>\\nJoomla! version: 3.9.22 (Outdated)\\nFOUND: http://ctf.rpca.ac.th/joomla/configuration.php-bak (CODE: 200)\\n\\n[+] JoomScan completed successfully.';
      }
    }, 1000);
  };

  document.addEventListener('click', function(e) {
    var tabWp = e.target.closest('#nav-item-wpscan');
    if (tabWp) {
      var tabJoom = document.getElementById('nav-item-joomscan');
      var panelWp = document.getElementById('panel-wpscan');
      var panelJoom = document.getElementById('panel-joomscan');
      if (panelWp && panelJoom) {
        panelWp.style.display = 'block';
        panelJoom.style.display = 'none';
        tabWp.classList.add('active');
        if (tabJoom) tabJoom.classList.remove('active');
      }
      return;
    }

    var tabJoom = e.target.closest('#nav-item-joomscan');
    if (tabJoom) {
      var tabWp2 = document.getElementById('nav-item-wpscan');
      var panelWp2 = document.getElementById('panel-wpscan');
      var panelJoom2 = document.getElementById('panel-joomscan');
      if (panelWp2 && panelJoom2) {
        panelWp2.style.display = 'none';
        panelJoom2.style.display = 'block';
        tabJoom.classList.add('active');
        if (tabWp2) tabWp2.classList.remove('active');
      }
      return;
    }

    var runWp = e.target.closest('#btn-run-wpscan');
    if (runWp) {
      startWebSim('wpscan');
      return;
    }

    var runJoom = e.target.closest('#btn-run-joomscan');
    if (runJoom) {
      startWebSim('joomscan');
      return;
    }
  });
})();
"""

# HTML fixes: add IDs to Run Simulation buttons
BUTTON_FIXES = {
    179: {
        # Panel sqlitest run button
        'sqlitest_btn': {
            'panel_id': 'panel-sqlitest',
            'btn_id': 'btn-run-sqlitest',
        },
        'cmdtest_btn': {
            'panel_id': 'panel-cmdtest',
            'btn_id': 'btn-run-cmdtest',
        },
    },
    180: {
        'wpscan_btn': {
            'panel_id': 'panel-wpscan',
            'btn_id': 'btn-run-wpscan',
        },
        'joomscan_btn': {
            'panel_id': 'panel-joomscan',
            'btn_id': 'btn-run-joomscan',
        },
    }
}

with app.app_context():
    from CTFd.plugins.tutorials import TutorialLesson
    db = app.db

    for lid, new_script in [(179, SCRIPT_179), (180, SCRIPT_180)]:
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        if not lesson:
            print(f"[!] Lesson {lid} not found")
            continue

        blocks = json.loads(lesson.content)
        val = blocks[1].get('value', '')

        # Step 1: Add IDs to Run Simulation buttons inside each panel
        fixes = BUTTON_FIXES[lid]
        for fix_key, fix_info in fixes.items():
            panel_id = fix_info['panel_id']
            btn_id = fix_info['btn_id']

            # Find the panel section and add ID to the Run Simulation button within it
            # Pattern: inside div id="panel-XXX", find button with "Run Simulation" that has no id
            panel_pattern = r'(id="' + re.escape(panel_id) + r'".*?)<button((?:(?!id=)[^>])*?)>(▶ Run Simulation)</button>'
            
            def add_btn_id(match):
                prefix = match.group(1)
                attrs = match.group(2)
                text = match.group(3)
                return f'{prefix}<button id="{btn_id}"{attrs}>{text}</button>'
            
            new_val = re.sub(panel_pattern, add_btn_id, val, count=1, flags=re.DOTALL)
            if new_val != val:
                print(f"  [+] Lesson {lid}: Added id='{btn_id}' to Run button in {panel_id}")
                val = new_val
            else:
                # Try simpler approach: just look for buttons without IDs near the panel
                print(f"  [~] Lesson {lid}: Complex pattern didn't match for {panel_id}, trying simpler approach...")

        # Step 2: Replace the entire script block with new event delegation script
        val = re.sub(r'<script>.*?</script>', '', val, flags=re.DOTALL)
        val = val + f'\n<script>{new_script}</script>'

        blocks[1]['value'] = val
        lesson.content = json.dumps(blocks, ensure_ascii=False)
        db.session.commit()
        print(f"[+] Lesson {lid} sandbox block updated with event delegation!")

    # Verify
    print("\n--- Verification ---")
    for lid in [179, 180]:
        lesson = db.session.query(TutorialLesson).filter_by(id=lid).first()
        blocks = json.loads(lesson.content)
        val = blocks[1].get('value', '')
        has_delegation = 'document.addEventListener' in val
        has_onclick = 'onclick=' in val.lower()
        has_iife = '(function()' in val
        btn_ids = re.findall(r'id="(btn-run-[^"]+)"', val)
        nav_ids = re.findall(r'id="(nav-item-[^"]+)"', val)
        print(f"Lesson {lid}: delegation={has_delegation}, onclick={has_onclick}, iife={has_iife}")
        print(f"  nav_ids: {nav_ids}, btn_ids: {btn_ids}")

    print("\n[DONE] Hard refresh (Ctrl+F5) to test!")
