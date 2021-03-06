import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { register } from '../../actions/authentication.actions';
import RegisterForm from '../../components/registerForm/registerForm.component';

class RegisterPage extends Component {
	constructor(props) {
		super(props);
		this.state = {
			first_name: '',
			last_name: '',
			email: '',
			password: '',
			username: ''
		};
	}

	renderRegisterForm() {
		return (
			<RegisterForm
				handleSubmit={this.onSubmit.bind(this)}
				handleChange={this.onChange.bind(this)}
				values=
					{{
						username: this.state.username,
						first_name: this.state.first_name,
						last_name: this.state.last_name,
						email: this.state.email,
						password: this.state.password
					}}
			/>
		);
	}

	onSubmit($event) {
		$event.preventDefault();

		const userData = {
			username: this.state.username,
			first_name: this.state.first_name,
			last_name: this.state.last_name,
			email: this.state.email,
			password: this.state.password
		};

		this.props.register(userData);
	}

	onChange($event) {
		this.setState({[$event.target.name]: $event.target.value});
	}

	render() {
		return (
			<div className='page-container'>
				<h1>Register</h1>
				{this.renderRegisterForm()}
			</div>
		);
	}
}

RegisterPage.propTypes = {
	register: PropTypes.func.isRequired
};

export default connect(null, {register})(RegisterPage);
