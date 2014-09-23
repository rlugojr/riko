# Pipe pipe_HrX5bjkv3BGEp9eSy6ky6g generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipefeedautodiscovery import pipe_feedautodiscovery
from pipe2py.modules.pipeloop import pipe_loop
from pipe2py.modules.pipesort import pipe_sort
from pipe2py.modules.pipetruncate import pipe_truncate
from pipe2py.modules.pipeoutput import pipe_output


def pipe_HrX5bjkv3BGEp9eSy6ky6g(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return [u'pipefeedautodiscovery', u'pipefetch', u'pipeloop', u'pipeoutput', u'pipesort', u'pipetruncate']

    forever = pipe_forever()

    # We need to wrap submodules (used by loops) so we can pass the
    # input at runtime (as we can to subpipelines)
    def pipe_sw_165(context=None, _INPUT=None, conf=None, **kwargs):
        # todo: insert submodule description here
        return pipe_fetch(
            context, _INPUT, conf={'URL': {'type': 'url', 'subkey': 'link'}})
    
    sw_149 = pipe_feedautodiscovery(
        context, forever, conf={'URL': {'type': 'url', 'value': 'file://data/edition.cnn.html'}})
    
    sw_157 = pipe_loop(
        context, sw_149, embed=pipe_sw_165, conf={'assign_part': {'type': 'text', 'value': 'all'}, 'assign_to': {'type': 'text', 'value': 'loop:fetch'}, 'emit_part': {'type': 'text', 'value': 'all'}, 'mode': {'type': 'text', 'value': 'EMIT'}, 'embed': {'type': 'module', 'value': {'type': 'fetch', 'id': 'sw-165', 'conf': {'URL': {'type': 'url', 'subkey': 'link'}}}}, 'with': {'type': 'text', 'value': ''}})
    
    sw_174 = pipe_sort(
        context, sw_157, conf={'KEY': [{'field': {'type': 'text', 'value': 'pubDate'}, 'dir': {'type': 'text', 'value': 'ASC'}}]})
    
    sw_191 = pipe_truncate(
        context, sw_174, conf={'count': {'type': 'number', 'value': '25'}})
    
    _OUTPUT = pipe_output(
        context, sw_191, conf={})
    
    return _OUTPUT


if __name__ == "__main__":
    pipeline = pipe_HrX5bjkv3BGEp9eSy6ky6g(Context())

    for i in pipeline:
        print i