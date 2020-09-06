# dfttk_tutorial
 Tutorials for dfttk (https://github.com/PhasesResearchLab/dfttk)

## Content

- [Installation](./1-Installation/Installation.md)
- [Configuration for DFTTK](./2-Configuration/Configuration.md)
- [Get Started](./3-Get_started/Get_started.md)

## Installation

### Create a virtual environment (Optional)

- Check the [python](https://www.python.org/) version

  ```shell
  python --version
  ```

  If it is python 2.x, please update the python to python 3.6+

  **PRL Group Notes:** For **ACI** account, please you just need to load the correct python by `module load python`

- Using [virtualenv](https://github.com/pypa/virtualenv)

  <details>
  <summary>Create Virtual Env By virtualenv</summary>
  <pre><code>#virtualenv --python=PYTHON_VERSION ENV_NAME
  virtualenv --python=python3.6 dfttk
  #Activate
  source dfttk/bin/activate
  #Deactivate
  deactivate</code></pre>
  </details>

- Using [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

  <details>
  <summary>Create Virtual Env Using conda</summary>
  <pre><code>#conda create -n ENV_NAME python=VERSION
  conda create -n dfttk python=3.6
  #Activate
  conda activate dfttk
  #Deactivate
  conda deactivate</code></pre>
</details>
  
  
  
  