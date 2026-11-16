Name:           apache-openmeetings
Version:        9.1.0
Release:        1%{?dist}
Summary:        Apache OpenMeetings web conferencing system
License:        Apache-2.0
URL:            https://openmeetings.apache.org/
Source0:        https://www.apache.org/dyn/closer.lua/openmeetings/9.1.0/bin/apache-openmeetings-9.1.0.tar.gz
BuildArch:      noarch

# OpenMeetings 9.1.0 requires Java 21
Requires:       java-21-openjdk-headless

# Disable debuginfo and jar repacking since this packages prebuilt binaries
%global debug_package %{nil}
%global __jar_repack %{nil}

%description
Apache OpenMeetings provides video conferencing, instant messaging, white board,
collaborative document editing and other groupware tools.

%prep
%setup -q -n apache-openmeetings-%{version}

%build
# Pre-compiled binary tarball; no build step required

%install
mkdir -p %{buildroot}/opt/openmeetings
cp -a * %{buildroot}/opt/openmeetings/

%files
%defattr(-,root,root,-)
/opt/openmeetings

%changelog
* Mon Nov 16 2026 Kenz Stewart <monkeybran12@fedoraproject.org> - 9.1.0-1
- Package Apache OpenMeetings 9.1.0 binary tarball for Fedora 45
