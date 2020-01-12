# Only needed during first-time setup:
pushd /tmp
    wget http://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-6-amd64.deb
    sudo dpkg -i couchbase-release-1.0-6-amd64.deb
popd

# Will install or upgrade packages
sudo apt-get update
sudo apt-get install libcouchbase-dev libcouchbase2-bin build-essential
