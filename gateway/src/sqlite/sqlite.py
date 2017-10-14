#!/usr/bin/env python
#Test sqlite datbase.
import commands

commands.getstatusoutput('chmod 777 create_table.sh')
commands.getstatusoutput('chmod 777 show.sh')
commands.getstatusoutput('./create_table.sh')

commands.getstatusoutput('./show.sh')
