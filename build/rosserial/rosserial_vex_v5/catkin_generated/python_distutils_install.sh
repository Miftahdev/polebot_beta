#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/miftah/polebot_beta/src/rosserial/rosserial_vex_v5"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/miftah/polebot_beta/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/miftah/polebot_beta/install/lib/python3/dist-packages:/home/miftah/polebot_beta/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/miftah/polebot_beta/build" \
    "/usr/bin/python3" \
    "/home/miftah/polebot_beta/src/rosserial/rosserial_vex_v5/setup.py" \
     \
    build --build-base "/home/miftah/polebot_beta/build/rosserial/rosserial_vex_v5" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/miftah/polebot_beta/install" --install-scripts="/home/miftah/polebot_beta/install/bin"
