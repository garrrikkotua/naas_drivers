from naas_drivers.driver import InDriver
from IPython.core.display import display, HTML
import markdown2


class Markdown(InDriver):
    """ Markdown generator lib"""

    def __open_or_read(self, data):
        read_data = data
        if "." in data:
            try:
                read_data = open(data, "r").read()
            except OSError:
                pass
        return read_data

    def convert(self, data, output_type="html"):
        data_read = self.__open_or_read(data)
        if output_type == "html":
            return markdown2.markdown(data_read)
        else:
            error_text = f"output {output_type} not supported for now"
            self.print_error(error_text)

    def display(self, data):
        data_read = self.__open_or_read(data)
        display(HTML(self.convert(data_read)))
