var path = require("path")
var webpack = require('webpack')
var BundleTracker = require('webpack-bundle-tracker')

module.exports = {
	context: __dirname,

	entry: {
		Main: './assets/js/Components/Main'
	},
	output: {
		path: path.resolve('./assets/bundles/'),
		filename: "[name].js"
	},

	plugins: [
		new BundleTracker({ filename: './webpack-stats.json' }),
	],

	module: {
		loaders: [
			{ test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader' }, // to transform JSX into JS
			{
				test: /\.css$/,
				loader: 'style!css!'
			},
			{
				test: /\.(png|jpg|gif)$/,
				loader:
					'file-loader'
			},
		],
		rules: [
			{ test: /\.css$/, use: ['style-loader', 'css-loader'] },
			{
				test: /\.(png|jpg|gif)$/,
				use: [
					{
						loader: 'file-loader',
						options: {}
					}
				]
			},

		]

	},

	resolve: {
		modulesDirectories: ['node_modules', 'bower_components'],
		extensions: ['.js', '.jsx']
	},
}
