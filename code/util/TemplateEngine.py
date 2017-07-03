# http://www.makotemplates.org/
from mako.template import Template

class TemplateEngine:

    @staticmethod
    def generate(templateFile, data):
        templateFile = open(templateFile, 'r')
        templateContent = templateFile.read()

        print(Template(templateContent).render(data="world"))

if __name__ == '__main__':
    TemplateEngine.generate('../../templates/sql/InsertAsSelect.sql','')
