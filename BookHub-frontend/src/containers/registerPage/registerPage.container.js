import React, {Component} from 'react';
import {connect} from 'react-redux';
import {register} from '../../actions/authentication.actions';
import RegisterForm from '../../components/registerForm/registerForm.component';

class RegisterPage extends Component {
	constructor(props) {
		super(props);
		this.state = {
			name: '',
			surname: '',
			email: '',
			password: ''
		};
	}

	renderRegisterForm() {
		return (
			<RegisterForm
				handleSubmit={this.onSubmit.bind(this)}
				handleChange={this.onChange.bind(this)}
				values=
					{{
						name: this.state.name,
						surname: this.state.surname,
						email: this.state.email,
						password: this.state.password
					}}
			/>
		);
	}

	onSubmit($event) {
		const userData =
			{
				name: this.state.name,
				surname: this.state.surname,
				email: this.state.email,
				password: this.state.password
			};

		this.props.register(userData);

		$event.preventDefault();
	}

	onChange($event) {
		this.setState({[$event.target.name]: $event.target.value});
	}

	render() {
		return (
			<div>
				{this.renderRegisterForm()}
			</div>
		);
	}
}

export default connect(null, {register})(RegisterPage);
