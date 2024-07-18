# %%
from os.path import join, expanduser
from emit_tools import load_EMIT_swath, extract_GLT, apply_GLT, ortho_xr

# %%
filename = expanduser(join("~", "Downloads", "EMIT_L2A_RFL_001_20240521T232728_2414216_003.nc"))

# %%
swath_ds = load_EMIT_swath(filename)
swath_ds

# %%
GLT_array = extract_GLT(swath_ds)
GLT_array

# %%
type(GLT_array)

# %%
GLT_array.shape

# %%
ortho_ds = ortho_xr(swath_ds)
ortho_ds

# %%
swath_array = swath_ds["reflectance"].data
swath_array

# %%
swath_array.shape

# %%
type(swath_array)

# %%
ortho_array = apply_GLT(swath_array, GLT_array)
ortho_array

# %%
type(ortho_array)

# %%
ortho_array.shape

# %%
ortho_array.squeeze().shape

# %%



