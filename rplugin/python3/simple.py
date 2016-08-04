import neovim
import time

@neovim.plugin
class SimplePlugin(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.rpc_export("SimpleRpc")
    def rpc(self, *args):
        self.nvim.command('echo "simple rpc"')

    @neovim.function('SimpleFunc')
    def func(self, args):
        self.nvim.command('echo "simple func"')

    @neovim.autocmd('BufEnter', pattern="*", eval='expand("<afile>")', sync=True)
    def autocmd(self, *args):
        self.nvim.command('echo "simple autocmd"')
