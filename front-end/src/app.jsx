import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter as Router, Route, Link, Redirect, Switch } from 'react-router-dom';
import { spring, AnimatedRoute ,AnimatedSwitch} from 'react-router-transition';
// layout
import Layout from 'component/layout/index.jsx'
// page
import Home from './page/home/index.jsx'
import Status from './page/status/index.jsx'


// we need to map the `scale` prop we define below
// to the transform style property
function mapStyles(styles) {
    return {
        opacity: styles.opacity,
        transform: `scale(${styles.scale})`,
    };
}

// wrap the `spring` helper to use a bouncy config
function bounce(val) {
    return spring(val, {
        stiffness: 330,
        damping: 22,
    });
}

// child matches will...
const bounceTransition = {
    // start in a transparent, upscaled state
    atEnter: {
        opacity: 0,
        scale: 1.2,
    },
    // leave in a transparent, downscaled state
    atLeave: {
        opacity: bounce(0),
        scale: bounce(0.8),
    },
    // and rest at an opaque, normally-scaled state
    atActive: {
        opacity: bounce(1),
        scale: bounce(1),
    },
};

class App extends React.Component{
    constructor(props){
        super(props);
    }


    render(){
        let LayoutRouter = (
            <Layout>
                <AnimatedSwitch
                    atEnter={bounceTransition.atEnter}
                    atLeave={bounceTransition.atLeave}
                    atActive={bounceTransition.atActive}
                    mapStyles={mapStyles}
                    className="route-wrapper"
                >
                    <Route exact path="/" component={Home}/>
                    <Route exact path="/home" component={Home}/>
                    <Route exact path="/status" component={Status}/>
                    {/*<Redirect exact from="/order" to="/order/index"/>*/}
                    {/*<Redirect exact from="/user" to="/user/index"/>*/}
                    {/*<Route component={ErrorPage}/>*/}
                </AnimatedSwitch>
            </Layout>
        );
        return (
            <Router>
                <Switch>
                    {/*<Route path="/login" component={Login}/>*/}
                    <Route path="/" render={ props => LayoutRouter}/>
                </Switch>
            </Router>
        )
    }
}

ReactDom.render(
    <App />,
    document.getElementById("app")
);