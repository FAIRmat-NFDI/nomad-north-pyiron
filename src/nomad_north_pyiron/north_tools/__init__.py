#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

pyiron_north_tool = NORTHTool(
    image='pyiron/pyiron:latest',
    description="""### **Pyiron**: Complex workflows made easy

    From rapid prototyping to high performance computing in materials science.
    [Homepage](https://pyiron.org/).""",
    short_description='Jupyterlab with pyiron installed',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='https://raw.githubusercontent.com/FAIRmat-NFDI/nomad-north-pyiron/refs/heads/main/src/nomad_north_pyiron/north_tools/pyiron/pyiron.png',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[
        {'email': 'lukas.pielsticker@physik.hu-berlin.de', 'name': 'Lukas Pielsticker'}
    ],
    mount_path='/home/jovyan',
    path_prefix='lab/tree',
    privileged=False,
    with_path=True,
    display_name='Pyiron',
)

pyiron = NorthToolEntryPoint(id_url_safe='pyiron', north_tool=pyiron_north_tool)
