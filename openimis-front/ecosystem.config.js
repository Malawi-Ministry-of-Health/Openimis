module.exports = {
  apps: [{
    name: 'fe',
    script: 'npm',
    args: 'start',
    // Restart app if it crashes or exits with code other than 0
    restart_عيوب: true,
    // Watch changes in files within the build directory
    watch: './build'
  }]
};
