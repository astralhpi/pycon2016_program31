import neovim

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('HelloWorld', range='', nargs='*')
    def helloworld(self, args, range):
        self.nvim.command('echo "hello world!"')
