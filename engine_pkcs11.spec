Summary: PKCS#11 engine for OpenSSL
Name: engine_pkcs11
Version: 0.1.7
Release: %mkrel 1
License: BSD
Group: System/Libraries
Source0: http://www.opensc-project.org/files/%{name}/%{name}-%{version}.tar.gz
Buildrequires: libp11-devel >= 0.2.1
Buildrequires: libopenssl-devel
URL: http://www.opensc.org/engine_pkcs11
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Engine_pkcs11 is an implementation of an engine for OpenSSL. It can be loaded
using code, config file or command line and will pass any function call by
openssl to a PKCS#11 module. Engine_pkcs11 is meant to be used with smart cards
and software for using smart cards in PKCS#11 format, such as OpenSC. Originaly
this engine was a part of OpenSC, until OpenSC was split into several small
projects for improved flexibility.

%prep
%setup -q
cat > README.mandriva <<EOF
In Mandriva, the engine file has been placed in the
%{_libdir}/openssl/engines directory instead of the default
%{_libdir}/engines. This was done so in order to match our openssl
installation.

Considering this new path, below is the suggested change to openssl.cnf
in order to use this engine:

openssl_conf = openssl_def

[openssl_def]
engines = engine_section

[engine_section]
pkcs11 = pkcs11_section

[pkcs11_section]
engine_id = pkcs11
dynamic_path = %{_libdir}/openssl/engines/engine_pkcs11.so
MODULE_PATH = %{_libdir}/opensc-pkcs11.so
init = 0

EOF

chmod 0644 README.mandriva

%build
%configure2_5x --with-enginesdir=%{_libdir}/openssl/engines
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}%{_libdir}/openssl/engines/*.a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/README doc/nonpersistent/wiki.out/* README.mandriva
%{_libdir}/openssl/engines/*
