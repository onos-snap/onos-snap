import snapcraft
import os

class XOnosBuck(snapcraft.BasePlugin):
    def build(self):
        super().build()
        os.environ['ONOS_ROOT'] = self.builddir
        print(os.environ['ONOS_ROOT'])
        command = ['tools/build/onos-buck']
        command.extend(['build', 'onos'])
        self.run(command)

        command = ['tar']
        command.extend(['-C', self.installdir])
        command.extend(['--strip-components', '1'])
        command.extend(['-zxf', 'buck-out/gen/tools/package/onos-package/onos.tar.gz'])
        self.run(command)
