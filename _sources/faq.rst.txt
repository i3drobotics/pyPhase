*******
FAQ
*******

No module named 'phase'
#######################

**Issue:**

.. code-block:: python
   
   ModuleNotFoundError: No module named 'phase'

**Cause:**

phase python module is not installed.

**Solution:**

.. code-block:: console

   pip install phase

Cannot load Phase library
#########################

**Issue:**

.. code-block:: python

   Exception: Cannot load Phase library. PHASE_DIR is set but path does not exist: C:\Program Files\Phase\bin

**Cause:**

Phase Library is not installed.

**Solution:**

   **Linux**

   Download debian package from `v0.0.20 release <https://github.com/i3drobotics/phase-dev/releases/tag/v0.0.20>`_.

   Install debian package using apt package manager:

   .. code-block:: console

      sudo apt install -f ./phase_vx.x.x-amd64.deb

   This should install to `/opt/i3dr/phase`

   **Windows**

   Download Windows installer from the `v0.0.20 release <https://github.com/i3drobotics/phase-dev/releases/tag/v0.0.20>`_.

   Install using the installer GUI, this should install to `C:\\Program Files\\i3DR\\Phase`
