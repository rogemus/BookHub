import React, {Component} from 'react';
import {connect} from 'react-redux';
import {login} from '../../actions/authentication.actions';
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

		this.props.login(userData);
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

export default connect(null, {login})(LoginPage);

