from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

pyiron = NORTHTool(
    short_description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-pyiron.',
    image='ghcr.io/FAIRmat-NFDI/nomad-north-pyiron:latest',
    description='Jupyter Notebook server in NOMAD NORTH for NOMAD plugin nomad-north-pyiron.',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'lukas.pielsticker@physik.hu-berlin.de', 'name': 'Lukas Pielsticker'}],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='pyiron',
)

north_tool_entry_point = NorthToolEntryPoint(
    id_url_safe='nomad_north_pyiron_pyiron', north_tool=pyiron
)
