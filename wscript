def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")
  conf.env['LIBPATH_HIREDIS']  = '../deps/hiredis'
  conf.env['LIB_HIREDIS']      = 'hiredis'

def build(bld):
  obj = bld.new_task_gen("cxx", "shlib", "node_addon", uselib='HIREDIS')
  obj.cxxflags = ["-I../deps", "-g", "-Wall"]
  obj.source = "hiredis.cc reader.cc"
  obj.target = "hiredis"
