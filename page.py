import streamlit as st
import mysql.connector

db=mysql.connector.connect(host="bakgs4ewc5wjhjigbt9w-mysql.services.clever-cloud.com",user="u6yovg764kskss2z",password="iWSZjK9HdgGfMmdZEUJp",database="bakgs4ewc5wjhjigbt9w")
c=db.cursor()
def show_data(i=0,n=0):
    l=True
    if n!=0:
             c.execute(f"select * from stock where (name={n} or id={i})")
             d=c.fetchall()
    elif i!=0:
            p="select * from stock where id = %s"
            c.execute(p,(i,))
            d=c.fetchall()         
    else:
        c.execute("select * from stock")
        d=c.fetchall()

    return d
def show_by_date(d='0'):
    c.execute(f"select * from stock where date=%s",(d))
    d=c.fetchall()
    return d
t=False
def login():
    st.title("Login")
    i_=st.text_input("Enter Username")
    p=st.text_input("Enter Password", type="password")
    if st.button("Login",type="primary"):
        if i_ and p:
            c.execute("SELECT id, password FROM user WHERE id = %s AND password = %s",(i_,p))
            result = c.fetchall()
            if result:
                st.write('s')
                st.session_state.page = "op"
                    
                    
def op():
    u = st.selectbox("Select",("select","add stock", "show stock","remove stock"))
    if u=="add stock":
        st.session_state.page = "add stock"
    elif u=="show stock":
        st.session_state.page = "show stock"
    elif u=="remove stock":
        st.session_state.page = "remove stock"
    elif st.button("next"):
            print("")
    elif st.button("back"):
        st.session_state.page = "login"
def addstock():
    st.title("add stock")
    n = st.text_input("name")
    i = st.text_input("id no.")
    q = st.text_input("qty")
    d = st.date_input("date")
    w = st.text_input("warranty period(in months)")
    cc = st.text_input("ok or not ok")
    s = st.text_input("specifications")
    l=st.button("insert")
    if l:
        if n and i and q:              
                c.execute('insert into stock values (%s,%s,%s,%s,%s,%s,%s)',(n,i,q,d,w,cc,s))
                db.commit()
                st.write('success')
                st.success('done')
                if st.button("back"):
                   st.session_state.page = "op"
    elif st.button("back"):
        st.session_state.page = "op"
def showstock():
    st.title("show stock")
    s=st.selectbox("Select Action", ("show by id","show by date","show all"))
    if s=="show by id":
        r=st.text_input("enter id no.")
        if r:
            d=show_data(r)
            st.table(d)
            if st.button("back"):
                st.session_state.page = "op"
    elif s=="show by date":
        r=st.text_input("enter room no.")
        d=st.date_input("enter date")
        if r or d:
            d=show_by_date(d)
            st.table(d)
            if st.button("back"):
                st.session_state.page = "op"
    elif s=="show all":
        d=show_data()
        st.table(d)
        st.title("more info")
        i=st.text_input("id")
        c.execute(f"select * from stock where id=%s",(i,))
        d=c.fetchall()
        c.execute(f"select month(curdate())")
        dt=c.fetchall()
        c.execute(f"select year(curdate())")
        dt2=c.fetchall()
        w=int(d[0][4])
        m1=int(d[0][3].split("-")[1])
        y1=int(d[0][3].split("-")[0])
        m2=dt[0][0]
        y2=dt2[0][0]
        r=y2-y1,m2-m1
        b=w-(r[0]*12+r[1])
        st.write(f"warranty period:{w} months({b} months remaining)")
        if st.button("back"):
                st.session_state.page = "op"
    elif st.button("back"):
        st.session_state.page = "op"
def removestock():
    st.title("remove stock")
    i=st.text_input("enter id.")
    c.execute(f"select * from stock where id=%s",(i,))
    d=c.fetchall()
    st.table(d)
    if st.button("confirm"):
        c.execute(f"delete from stock where id=%s",(i,))
        db.commit()
        st.success("deleted")
        if st.button("back"):
            st.session_state.page = "op"
    elif st.button("back"):
            st.session_state.page = "op"
def close():
    db.close()       
    
    
    
    
