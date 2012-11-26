# VHostApp.py
#
# Application to manage Virtual Hosts
#
#


class VHostApp():

    def __init__(self, project):
        self.project = project
        # here we handle the command line input and test it for validity,
        # if there is an issue, we end the program and spit out errors.
    def print_name(self):
        print "<VirtualHost *:80>\n\t\t<IfModule mod_expires.c>\n\t\t\t\tExpiresActive Off\n\t\t</IfModule>\n\t\t##SSLEngine off\n\t\tServerAlias %s\n\n\t\tDocumentRoot /var/www/html/%s\n\t\tErrorLog logs/%s-error_log\n\t\tCustomLog logs/%s-access_log combined\n</VirtualHost>" % (self.project, self.project, self.project, self.project)


def main():

    c = VHostApp('myapp')
    c.print_name()

main()