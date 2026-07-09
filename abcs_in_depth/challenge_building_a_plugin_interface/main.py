from abc import ABC, abstractmethod

class LegacyXmlExporter:
    def export(self, data):
        items = "".join(f"<item>{row}</item>" for row in data)
        return f"<root>{items}</root>"

    def get_format(self):
        return "XML"

# Defining the plugin ABC
class ExporterPlugin(ABC):
    @abstractmethod
    def export(self, data):
        pass

    @abstractmethod
    def get_format(self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is ExporterPlugin:
            has_export = any("export" in klass.__dict__ for klass in subclass.__mro__)
            has_format = any("get_format" in klass.__dict__ for klass in subclass.__mro__)
            if has_export and has_format:
                return True
        return NotImplemented

# Concrete markdown exporter
class MarkdownExporter(ExporterPlugin):
    def export(self, data):
        return "\n".join(f"- {item}" for item in data)

    def get_format(self):
        return "Markdown"

# Registering the legacy exporter as a virtual subclass
ExporterPlugin.register(LegacyXmlExporter)

md_exporter = MarkdownExporter()
xml_exporter = LegacyXmlExporter()

md_is_plugin = isinstance(md_exporter, ExporterPlugin)
xml_is_plugin = isinstance(xml_exporter, ExporterPlugin)

print(md_is_plugin, xml_is_plugin)