debug: setup_dev
	echo "MuzzMan Lib"
	cd muzzman-lib;make
	echo "End MuzzMan Lib\n"
	echo ""
	echo "Modules"
	cd modules;make --always-make
	echo "End Modules"
	echo ""
	echo ""
	echo "MuzzMan egui"
	cd muzzman-egui;make
	echo "End MuzzMan egui"

run: debug
	cd muzzman-egui;make run

release: setup_dev
	echo "MuzzMan Lib"
	cd muzzman-lib;make release
	echo "End MuzzMan Lib\n"
	echo ""
	echo "Modules"
	cd modules;make --always-make release
	echo "End Modules"
	echo ""
	echo ""
	echo "MuzzMan egui"
	cd muzzman-egui;make release
	echo "End MuzzMan egui"

clean:
	cd muzzman-lib;make clean
	cd modules;make --always-make clean
	cd muzzman-egui;make clean

setup_dev:
	git submodule init
	git submodule update --recursive
