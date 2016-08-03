import neovim

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('helloworld')
    def helloworld(self, args):
        self.nvim.command('echo "hello world!"')


    @neovim.command('HelloWorld', range='', nargs='*')
    def helloworld_command(self, args, range):
        self.nvim.helloworld()
