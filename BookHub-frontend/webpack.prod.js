const webpack = require('webpack');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const cssnano = require('cssnano');
const HardSourceWebpackPlugin = require('hard-source-webpack-plugin');

const base = require('./webpack.make')();

module.exports = Object.assign(
	{},
	base,
	{
		plugins: [
			...base.plugins,
			new UglifyJsPlugin({
				parallel: true,
				cache: true,
				uglifyOptions: {
					mangle: true
				}
			}),
			new OptimizeCssAssetsPlugin({
				assetNameRegExp: /\.css$/g,
				cssProcessor: cssnano,
				cssProcessorOptions: {
					discardComments: {
						removeAll: true
					}
				},
				canPrint: true
			}),
			new HardSourceWebpackPlugin()
		],
		devtool: 'none'
	}
);
