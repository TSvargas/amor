import streamlit as st 
from unicodedata import normalize
import time
from PIL import Image

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)



st.header(':rainbow[Nossa linha do tempo] :heart: :heart:' )
col1, col2, col3, col4 = st.columns(4)

#aqui você declara as "colunas" e após o sinal de "=" seus titulos, respectivamente:

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11, tab12, tab13, tab14, tab15, tab16, tab17, tab18 = st.tabs(['27/12/2022', '02/02/2023', '10/05/2023', '13/05/2023', '15/05/2023', '09/06/2023', '11/07/2023', '20/08/2023', '02/09/2023', '21/10/2023 à 22/10/2023', '10/12/2023', '30/12/2023', '02/01/2024', '08/02/2024', '14/02/2024', '15/02/2024', '19/02/2024', 'Eterno'])

with tab1:
    st.subheader('A primeira mensagem')
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        st.image('primeiramsg.png',  width= 400)
        st.caption('KKKKKKKKKK marcante')

with tab2:
    st.subheader('Nossa primeira vez pessoalmente (confesso que poderia ter sido melhor)')
    st.write('Não tem registros nossos desse dia, então toma essa gatinha!!!!!')
    st.image('gatinha.png', width= 400)
    st.caption('Misericódia!!!!!!!!!!' ':heart_eyes:')

with tab3:
    st.subheader('Eu dando em cima de você e tu tb KKKKKKKKKKK')
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("rs.png", width= 300)
    with col3:
        st.image('ataque1.png', width= 300)
    st. image('ataque2.png', width= 300)

with tab4:
    st.subheader('Nosso primeiro encontro :sob: :heart: :heart:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col3:
        st.image("primeiroencontro.png", width= 300)
    st.caption('Você tava linda demais, demos um abraço gostoso nesse dia e aí eu te conquistei de vez, rs')

with tab5:
    st.subheader('O primeiro "eu te amo", rs')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('teamo.png', width= 400)
    st.caption('Eu que falei, tá?!! :sunglasses:')

with tab6:
    st.subheader('Nossa primeira "discussão" :sleepy:')
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        st.image('discussao.png', width= 300)
    st.caption('Eu me arrependo mt até hj, mds, errei mt, fui mlk')

with tab7:
    st.subheader('A primeira vez na sua casa :grin: :grin:')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('suacasa1.png', width= 200)
    with col2:
        st.image('suacasa2.png',width= 200)
    with col3:
        st.image('suacasa3.png', width= 200)
    st.caption('Saudade desse carinho')

with tab8:
    st.subheader('Primeira ida na igreja juntos e almoço com a sua família')
    col1, col2, col3, col4 = st.columns(4)
    with col2:
        st.image('almoco1.png', width= 300)
    
with tab9:
    st.subheader('Nosso primeiro beijo')
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    with col2:
        st.image('primeirobjo.png', width= 400)

with tab10:
    st.subheader('Primeira "viagem" juntos')
    st.image('viagem1.png', width= 800)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('viagem2.png', width= 600)
    
with tab11:
    st.subheader("Acamp's")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('acamps1.png', width= 400)
    st.caption('O trio de la pelota nunca será esquecido! :heart: ')

with tab12:
    st.subheader('Chá de revelação de Leninha')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('helena1.png', width=400)
        st.image('helena2.png', width= 400)

with tab13:
    st.subheader('Sua primeira despedida, com a família toda na igreja	:cry:')
    st.write('Também não tenho registros :sob: :sob:')
    st.write('Toma essa gostosa')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('gatinha2.jpeg', width=400)
    st.title('ta poxa 	:yum: 	:face_with_spiral_eyes: 	:face_with_spiral_eyes: 	:drooling_face: 	:drooling_face:')

with tab14:
    st.subheader('Sua volta :no_good: :see_no_evil:	:see_no_evil:')
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col2:
        st.image('suavolta1.png', width= 400)
        st.image('suavolta2.png', width= 400)
    
with tab15:
    st.subheader('NOSSO NAMORO!!	:tada: 	:tada: 	:heart_eyes: 	:sneezing_face: 	:revolving_hearts: 	:two_hearts: 	:partying_face: 	:partying_face:')
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.image('namoro1.png', width= 300)
    with col3:
        st.image('namoro2.png', width= 300)
    with col1:
        st.image('namoro3.png', width= 300)
    with col3:
        st.image('namoro4.png', width= 300)
    with col1:
        st.image('namoro5.png', width= 300)
    st.caption('O desespero foi recompensado, rs')

with tab16:
    st.subheader('Seu niveeer :partying_face: :partying_face: :partying_face: :partying_face:')
    st.write('Estávamos lindos dms, slkkk')
    st.write('Te dei logo um buquêzão pra ficar esperta :face_with_hand_over_mouth:')
    col1, col2, col3, col4= st.columns(4)
    with col1:
        st.image('niver1.png', width= 400)
    with col3:
        st.image('niver2.png', width= 400)
    with col1:
        st.image('niver3.png', width= 400)
    with col3:
        st.image('niver4.png', width= 400)
    st.write('Esse dia foi muito importante pra mim, estar no seu aniversário de 15 anos em meio a sua família e junto com a minha foi mágico. Vc princesa dms tb... Me dificulta')

with tab17:
    st.subheader('Sua despedida para não voltar tão cedo :weary: :cry: ')
    st.write('Essa aqui foi oficial')
    col1, col2, col3, col4, col5, col6= st.columns(6)
    with col2:
         st.image('despedida.png', width= 500)
    st.write('Pelo menos foi mtttt bom, assistimos filme juntinhos, te vi toda gostosa com meu vestido preferido e... Apertei um balãoKKKKKKKKKKKKKKKKKKKK')

with tab18:
    st.subheader('Agora um pouco do que foi e vai ser eterno :heart:')
    col1, col2, col3, col4, col5, col6= st.columns(6)
    with col1:
        st.image('encontro1.png', width= 300)
    with col4:
        st.image('encontro2.png', width= 300)
    with col1:
        st.image('encontro3.png', width= 300)
    with col4:
        st.image('encontro4.png', width=300)
    with col4:
        st.image('encontro5.png', width=300)
    with col4:
        st.image('encontro6.png', width=300)
    with col1:
        st.image('encontro7.png', width=300)
    
    st.write('FIMM!!')
    st.write('Te amo mozão')
