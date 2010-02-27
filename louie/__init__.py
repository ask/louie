"""Signal dispatching mechanism"""

__all__ = [
    'dispatcher',
    'error',
    'plugin',
    'robustapply',
    'saferef',
    'sender',
    'signal',
    'version',
    
    'connect',
    'disconnect',
    'get_all_receivers',
    'reset',
    'send',
    'send_exact',
    'send_minimal',
    'send_robust',

    'install_plugin',
    'remove_plugin',
    'Plugin',
    'QtWidgetPlugin',
    'TwistedDispatchPlugin',

    'Anonymous',
    'Any',

    'All',
    'Signal',
    ]

import louie.dispatcher, louie.error, louie.plugin, louie.robustapply, \
       louie.saferef, louie.sender, louie.signal, louie.version

from louie.dispatcher import \
     connect, disconnect, get_all_receivers, reset, \
     send, send_exact, send_minimal, send_robust

from louie.plugin import \
     install_plugin, remove_plugin, Plugin, \
     QtWidgetPlugin, TwistedDispatchPlugin

from louie.sender import Anonymous, Any

from louie.signal import All, Signal


from louie.version import __version__, __author__, __contact__, __homepage__
from louie.version import __docformat__
