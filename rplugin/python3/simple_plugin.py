import neovim

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.function('helloworld', sync=True)
    def helloworld(self, args):
        self.nvim.command('echo "hello world!"')
