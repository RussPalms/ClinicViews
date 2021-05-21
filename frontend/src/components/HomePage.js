import React, { Component } from "react";
import {
    BrowserRouter as Router, 
    Switch, 
    Route, 
    Link, 
    Redirect 
} from "react-router-dom";

class HomePage extends Component{
    render() {
        return (
            <Router>
                <Switch>
                    <Route
                        exact path="/"
                        render={() => {
                            return (
                            <div>
                                hello react
                            </div>
                            )
                        }}
                    />
                </Switch>
            </Router>
        );
    }
}

export default HomePage;