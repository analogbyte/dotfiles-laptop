import i3

displays = [display for display in i3.get_outputs() if display['active']]
workspaces = i3.get_workspaces()

if len(displays) == 2:
    for workspace in workspaces:
        i3.workspace(workspace['name'])
        i3.command('move', 'workspace to output right')
