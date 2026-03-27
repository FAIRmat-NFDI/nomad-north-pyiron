def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails for the north tool
    from nomad_north_pyiron.north_tools import pyiron

    assert (
        pyiron.id_url_safe == 'pyiron'
        or pyiron.id == 'nomad_north_pyiron.north_tools:pyiron'
    ), 'NORTHtool entry point has incorrect id or id_url_safe'
