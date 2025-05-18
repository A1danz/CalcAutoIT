from helper.base_helper import BaseHelper


class HeaderHelper(BaseHelper):
    def get_header(self):
        text_elem = self.window.child_window(auto_id="Header", control_type="Text")
        text_elem.wait('visible', timeout=5)

        return text_elem.window_text()