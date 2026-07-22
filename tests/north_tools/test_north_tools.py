def test_importing_north_tool():
    # this will raise an exception if pydantic model validation fails
    from nomad_north_pyiron.north_tools import pyiron
 
    expected_id = 'pyiron'
    assert (
        pyiron.id_url_safe == expected_id
        or pyiron.id == 'nomad-north-pyiron'
    ), 'NORTHTool entry point has incorrect id or id_url_safe'