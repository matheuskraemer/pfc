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
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/geonav_transform"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/matheus/Projects/pfc/dev/ros_kinetic/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/matheus/Projects/pfc/dev/ros_kinetic/install/lib/python2.7/dist-packages:/home/matheus/Projects/pfc/dev/ros_kinetic/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/matheus/Projects/pfc/dev/ros_kinetic/build" \
    "/usr/bin/python" \
    "/home/matheus/Projects/pfc/dev/ros_kinetic/src/ROS_quadrotor_simulator/geonav_transform/setup.py" \
    build --build-base "/home/matheus/Projects/pfc/dev/ros_kinetic/build/ROS_quadrotor_simulator/geonav_transform" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/matheus/Projects/pfc/dev/ros_kinetic/install" --install-scripts="/home/matheus/Projects/pfc/dev/ros_kinetic/install/bin"
