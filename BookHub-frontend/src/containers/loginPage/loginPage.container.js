import React, {Component} from 'react';
import {connect} from 'react-redux';
import {withRouter} from 'react-router';
import {postUserCredential} from '../../actions/authentication.actions';
import LoginForm from '../../components/loginForm/loginForm.component';

class LoginPage extends Component {
	constructor(props) {
		super(props);

		this.state = {
			username: '',
			password: ''
		};
	}

	renderLoginForm() {
		return (
			<LoginForm
				handleSubmit={this.onSubmit.bind(this)}
				handleChange={this.onChange.bind(this)}
				values={{username: this.state.username, password: this.state.password}}
			/>
		);
	}

	onSubmit($event) {
		$event.preventDefault();

		const userData = {
			username: this.state.username,
			password: this.state.password
		};

		this.props.postUserCredential(userData)
			.then(() => {
				this.props.history.push('/');
			});
	}

	onChange($event) {
		this.setState({[$event.target.name]: $event.target.value});
	}

	render() {
		return (
			<div>
				{this.renderLoginForm()}
			</div>
		);
	}
}

export default withRouter(connect(null, {postUserCredential})(LoginPage));

