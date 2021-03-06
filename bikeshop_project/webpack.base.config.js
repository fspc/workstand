const path = require('path');
const autoprefixer = require('autoprefixer');
require('babel-polyfill');

module.exports = {
  context: __dirname,

  entry: {
    signin: './assets/js/index',
    members: './assets/js/members/index',
    babelPolyfill: 'babel-polyfill',
  },

  output: {
    path: path.resolve('./assets/bundles/'),
    filename: '[name]-[hash].js',
  },

  plugins: [

  ], // add all common plugins here

  module: {
    loaders: [],
  },

  resolve: {
    modulesDirectories: [
      'node_modules',
      'bower_components',
    ],
    extensions: ['', '.js', '.jsx', '.scss'],
  },
  postcss: [autoprefixer],
};
