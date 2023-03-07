phy_device=tf.config.experimental.list_physical_devices("GPU")
print("num of devices: ",len(phy_device))
tf.config.experimental.set_memory_growth(phy_device[0],True)
