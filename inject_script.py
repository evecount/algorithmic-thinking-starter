import os
import re

html_path = r'D:\NTU_DSA_Workbook\docs\index.html'
md_path = r'D:\NTU_DSA_Workbook\NTU_DSA_Night_1_Dynamite_Script.md'

with open(md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Super simple markdown to HTML conversion for this specific script
html_script = md_content.replace('\n', '<br>')
html_script = re.sub(r'# (.*?)<br>', r'<h3>\1</h3>', html_script)
html_script = re.sub(r'\[TIMING:(.*?)\]', r'<div style="color: #f9ab00; font-weight: bold; font-size: 0.85rem;">[TIMING:\1]</div>', html_script)
html_script = re.sub(r'\[STAGE CUE:(.*?)\]', r'<div style="color: #00e1ff; font-style: italic; font-size: 0.85rem; margin-bottom: 8px;">[STAGE CUE:\1]</div>', html_script)

sidebar_html = f"""
    <!-- PRESENTER MODE SLIDE-OUT -->
    <div id="presenter-sidebar" style="position: fixed; top: 0; right: -450px; width: 450px; height: 100vh; background: rgba(10, 15, 25, 0.95); backdrop-filter: blur(20px); border-left: 1px solid rgba(0, 225, 255, 0.2); transition: right 0.3s ease-in-out; z-index: 9999; overflow-y: auto; padding: 2rem; box-shadow: -10px 0 30px rgba(0,0,0,0.5);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; position: sticky; top: 0; background: rgba(10, 15, 25, 0.95); padding-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); z-index: 2;">
        <h2 style="margin: 0; color: #fff; font-size: 1.2rem;">🎤 Presenter Script</h2>
        <button onclick="togglePresenterMode()" style="background: none; border: none; color: #94a3b8; font-size: 1.5rem; cursor: pointer;">&times;</button>
      </div>
      <div style="color: #e2e8f0; font-size: 1.05rem; line-height: 1.6;">
        {html_script}
      </div>
    </div>

    <button onclick="togglePresenterMode()" style="position: fixed; bottom: 2rem; right: 2rem; background: #00e1ff; color: #000; border: none; border-radius: 50px; padding: 0.8rem 1.5rem; font-weight: bold; font-family: 'Outfit', sans-serif; cursor: pointer; box-shadow: 0 4px 15px rgba(0, 225, 255, 0.4); z-index: 9998; transition: transform 0.2s;">
      👁️ Toggle Presenter Mode
    </button>

    <script>
      let presenterOpen = false;
      function togglePresenterMode() {{
        presenterOpen = !presenterOpen;
        const sidebar = document.getElementById('presenter-sidebar');
        if (presenterOpen) {{
          sidebar.style.right = '0';
        }} else {{
          sidebar.style.right = '-450px';
        }}
      }}
    </script>
"""

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Only inject if not already injected
if '<!-- PRESENTER MODE SLIDE-OUT -->' in html_content:
    # Remove existing block
    html_content = re.sub(r'<!-- PRESENTER MODE SLIDE-OUT -->.*?</script>', '', html_content, flags=re.DOTALL)

new_html = html_content.replace('</body>', sidebar_html + '\n</body>')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Successfully updated presenter mode slide-out in docs/index.html")
