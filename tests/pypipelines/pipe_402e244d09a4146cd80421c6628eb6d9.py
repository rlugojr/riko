# Pipe pipe_402e244d09a4146cd80421c6628eb6d9 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetchdata import pipe_fetchdata
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.piperegex import pipe_regex
from pipe2py.modules.pipeoutput import pipe_output


def pipe_402e244d09a4146cd80421c6628eb6d9(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipefetchdata', u'pipeoutput', u'piperegex', u'piperename']

    forever = pipe_forever()

    sw_572 = pipe_fetchdata(
        context, forever, conf={'URL': {'type': 'url', 'value': 'file://data/www.bbc.co.uk_programmes_b006mvlc_episodes_player.xml'}, 'path': {'type': 'text', 'value': 'episode'}})
    
    sw_587 = pipe_rename(
        context, sw_572, conf={'RULE': [{'field': {'type': 'text', 'value': 'programme.title'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'title'}}, {'field': {'type': 'text', 'value': 'programme.pid'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'link'}}, {'field': {'type': 'text', 'value': 'programme.short_synopsis'}, 'op': {'type': 'text', 'value': 'copy'}, 'newval': {'type': 'text', 'value': 'description'}}]})
    
    sw_598 = pipe_regex(
        context, sw_587, conf={'RULE': [{'field': {'type': 'text', 'value': 'link'}, 'match': {'type': 'text', 'value': '(.*)'}, 'replace': {'type': 'text', 'value': 'http://www.bbc.co.uk/programmes/$1'}}]})
    
    _OUTPUT = pipe_output(
        context, sw_598, conf={})
    
    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_402e244d09a4146cd80421c6628eb6d9(Context())

    for i in pipeline:
        print i