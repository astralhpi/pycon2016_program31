import neovim
import time

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.rpc_export("HelloWorld")
    def helloworld_rpc(self, *args):
        self.nvim.call('HelloWorld')

    @neovim.function('HelloWorld', sync=True)
    def helloworld(self, args):
        time.sleep(5000)
        self.nvim.command('echo "hello world!"')
        return 0

    @neovim.function('AsyncHelloWorld', sync=False)
    def async_helloworld(self, args):
        time.sleep(5000)
        self.nvim.command('echo "hello world!"')
        return 0


    @neovim.command('HelloWorld', range='', nargs='*')
    def helloworld_command(self, args, range):
        self.nvim.call('HelloWorld')
