srpm:
	dnf -y install rpmdevtools
	spectool -g -R openmeetings.spec
	rpmbuild -bs --define "_sourcedir $(PWD)" --define "_srcrpmdir $(outdir)" openmeetings.spec
