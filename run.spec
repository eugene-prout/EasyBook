# -*- mode: python -*-

block_cipher = None


a = Analysis(['run.py'],
             pathex=['C:\\Users\\EugeneProut\\Documents\\EasyBook'],
             binaries=[],
             datas=[],
             hiddenimports=["flask_wtf",
                            "flask_sqlalchemy",
                            "flask.views",
                            "flask.signals",
                            "flask_restful.utils",
                            "flask.helpers",
                            "flask_restful.representations",
                            "flask_restful.representations.json",
                            "sqlalchemy.orm",
                            "sqlalchemy.event",
                            "sqlalchemy.ext.declarative",
                            "sqlalchemy.engine.url",
                            "sqlalchemy.connectors.mxodbc",
                            "sqlalchemy.connectors.mysqldb",
                            "sqlalchemy.connectors.zxJDBC",
                            "sqlalchemy.connectorsodbc.py",
                            "sqlalchemy.dialects.sqlite.base",
                            "sqlalchemy.dialects.sqlitesqlite.py",
                            "sqlalchemy.dialects.sybase.base",
                            "sqlalchemy.dialects.sybase.mxodbc",
                            "sqlalchemy.dialects.sybaseodbc.py",
                            "sqlalchemy.dialects.sybasesybase.py",
                            "sqlalchemy.engine.base",
                            "sqlalchemy.engine.default",
                            "sqlalchemy.engine.interfaces",
                            "sqlalchemy.engine.reflection",
                            "sqlalchemy.engine.result",
                            "sqlalchemy.engine.strategies",
                            "sqlalchemy.engine.threadlocal",
                            "sqlalchemy.engine.url",
                            "sqlalchemy.engine.util",
                            "sqlalchemy.event.api",
                            "sqlalchemy.event.attr",
                            "sqlalchemy.event.base",
                            "sqlalchemy.event.legacy",
                            "sqlalchemy.event.registry",
                            "sqlalchemy.events",
                            "sqlalchemy.exc",
                            "sqlalchemy.ext.associationproxy",
                            "sqlalchemy.ext.automap",
                            "sqlalchemy.ext.compiler",
                            "sqlalchemy.ext.declarative.api",
                            "sqlalchemy.ext.declarative.base",
                            "sqlalchemy.ext.declarative.clsregistry",
                            "sqlalchemy.ext.horizontal_shard",
                            "sqlalchemy.ext.hybrid",
                            "sqlalchemy.ext.instrumentation",
                            "sqlalchemy.ext.mutable",
                            "sqlalchemy.ext.orderinglist",
                            "sqlalchemy.ext.serializer",
                            "sqlalchemy.inspection",
                            "sqlalchemy.interfaces",
                            "sqlalchemy.log",
                            "sqlalchemy.orm.attributes",
                            "sqlalchemy.orm.base",
                            "sqlalchemy.orm.collections",
                            "sqlalchemy.orm.dependency",
                            "sqlalchemy.orm.deprecated_interfaces",
                            "sqlalchemy.orm.descriptor_props",
                            "sqlalchemy.orm.dynamic",
                            "sqlalchemy.orm.evaluator",
                            "sqlalchemy.orm.events",
                            "sqlalchemy.orm.exc",
                            "sqlalchemy.orm.identity",
                            "sqlalchemy.orm.instrumentation",
                            "sqlalchemy.orm.interfaces",
                            "sqlalchemy.orm.loading",
                            "sqlalchemy.orm.mapper",
                            "sqlalchemy.orm.path_registry",
                            "sqlalchemy.orm.persistence",
                            "sqlalchemy.orm.properties",
                            "sqlalchemy.orm.query",
                            "sqlalchemy.orm.relationships",
                            "sqlalchemy.orm.scoping",
                            "sqlalchemy.orm.session",
                            "sqlalchemy.orm.state",
                            "sqlalchemy.orm.strategies",
                            "sqlalchemy.orm.strategy_options",
                            "sqlalchemy.orm.sync",
                            "sqlalchemy.orm.unitofwork",
                            "sqlalchemy.orm.util",
                            "sqlalchemy.pool",
                            "sqlalchemy.processors",
                            "sqlalchemy.schema",
                            "sqlalchemy.sql.annotation",
                            "sqlalchemy.sql.base",
                            "sqlalchemy.sql.compiler",
                            "sqlalchemy.sql.ddl",
                            "sqlalchemy.sql.default_comparator",
                            "sqlalchemy.sql.dml",
                            "sqlalchemy.sql.elements",
                            "sqlalchemy.sql.expression",
                            "sqlalchemy.sql.functions",
                            "sqlalchemy.sql.naming",
                            "sqlalchemy.sql.operators",
                            "sqlalchemy.sql.schema",
                            "sqlalchemy.sql.selectable",
                            "sqlalchemy.sql.sqltypes",
                            "sqlalchemy.sql.type_api",
                            "sqlalchemy.sql.util",
                            "sqlalchemy.sql.visitors",
                            "sqlalchemy.types",
                            "sqlalchemy.util._collections",
                            "sqlalchemy.util.compat",
                            "sqlalchemy.util.deprecations",
                            "sqlalchemy.util.langhelpers",
                            "sqlalchemy.util.queue",
                            "sqlalchemy.util.topological",
                            "flask_sqlalchemy._compat"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)


def extra_datas(mydir):
    def rec_glob(p, files):
        import os
        import glob
        lst = glob.glob(p)
        for d in lst:
            if os.path.isfile(d):
                files.append(d)
            rec_glob("%s/*" % d, files)
    files = []
    rec_glob("%s/*" % mydir, files)
    _extra_datas = []
    # tuple(_extra_datas)
    for f in files:
        _extra_datas.append(tuple([f, f, 'DATA']))
        print(tuple([f, f, 'DATA']))

    return _extra_datas

a.datas += extra_datas("app")


pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='EasyBook',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='EasyBook')
