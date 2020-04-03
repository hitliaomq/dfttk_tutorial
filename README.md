# dfttk_tutorial
 Tutorials for dfttk (https://github.com/PhasesResearchLab/dfttk)

## Content

- [Installation](#Installation)
- [Configuration for DFTTK](https://github.com/hitliaomq/dfttk_tutorial/blob/master/config)
- [Get Started](https://github.com/hitliaomq/dfttk_tutorial/tree/master/get_started)

## Installation

### Create a virtual environment (Optional)

- Check the [python](https://www.python.org/) version

  ```shell
  python --version
  ```

  If it is python 2.x, please update the python to python 3.6+

  **PRL Group Notes:** For **ACI** account, please you just need to load the correct python by `module load python`

- Using [virtualenv](https://github.com/pypa/virtualenv)

  ```html
  <details>
      <summary>Create virtual environment by virtualenv</summary>
      ```bash
      #virtualenv --python=PYTHON_VERSION ENV_NAME
  	virtualenv --python=python3.6 dfttk
  	#Activate
  	source dfttk/bin/activate
  	#Deactivate
  	deactivate
      ```
  </details>
  ```

  

  

  

  ```shell
  #virtualenv --python=PYTHON_VERSION ENV_NAME
  virtualenv --python=python3.6 dfttk
  #Activate
  source dfttk/bin/activate
  #Deactivate
  deactivate
  ```

- Using [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

  ```shell
  #conda create -n ENV_NAME python=VERSION
  conda create -n dfttk python=3.6
  #Activate
  conda activate dfttk
  #Deactivate
  conda deactivate
  ```

  