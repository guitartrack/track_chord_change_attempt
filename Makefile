clean:
	rm -rf build 1.0.0.zip

create_build_map:
	mkdir build

install_app:
	cp track_chord_change_attempt/* build/

install_dependencies:
	pip install -r requirements.txt -t build

invoke:
	sam local invoke --event test.json

test: clean create_build_map install_app install_dependencies invoke

package: clean create_build_map install_app install_dependencies
	cd build && zip -r ../1.0.0.zip *
