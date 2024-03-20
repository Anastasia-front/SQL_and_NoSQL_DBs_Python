CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    status_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY (status_id) REFERENCES status(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);


-- id|title                                        |description                                                                                                                                                                                           |status_id|user_id|
-- --+---------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------+-------+
--  1|Speak new fact board difference executive.   |Good share doctor home policy feeling pressure. Animal huge benefit may career section.¶Research force along finally above local already.                                                             |        3|      1|
--  2|Decision wide before loss.                   |Before price society simply plant debate smile. Money baby hotel forward particular worry contain.¶Scientist stop director strong. Card painting respond develop hour.                                |        1|      2|
--  3|Message western year him keep.               |First each describe weight. Other level physical test. Activity become clearly help life employee a your.                                                                                             |        2|      5|
--  4|Evidence turn the recognize reason.          |Study military end political cost. Identify loss company explain white. Someone describe simply during some television recently.                                                                      |        1|      5|
--  5|Miss wall magazine.                          |Six alone include along. Show similar build range defense action. Throughout feeling hair seven pay long feel.¶Collection may fine onto recently hear spend. Thought few research available today yes.|        2|      1|
--  6|Prove major method mouth.                    |Him eye accept language. Nature student organization floor do discuss. Series relationship culture drive successful change off tax.¶Until short quite message top area fund. Glass group expert wish. |        1|      1|
--  7|Fire suggest to thus old she oil would.      |Discover page fall official thank entire yet. Shoulder nature third their concern guy study leave. Strong ground small past though.                                                                   |        1|      4|
--  8|Beyond short hold future within.             |Draw others fight scene size.¶As send stuff drop black sort political. Hospital not arm need how meet upon here.                                                                                      |        2|      6|
--  9|Mention behind full hundred thousand mention.|Discussion from view section risk. Good build husband rich arm.¶Food care popular discover. Author follow school true drive smile.                                                                    |        2|      1|
-- 10|Visit standard pretty.                       |Often make water. Choice art building piece certain break even participant. Size bit best possible instead tend.¶Difficult hope good employee quickly technology catch. No read particularly.         |        1|      5|