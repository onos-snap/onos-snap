import snapcraft

class XOnosBuck(snapcraft.BasePlugin):
    def build(self):
        super().build()
        self.run(['../../../parts/plugins/build.sh', self.installdir])
