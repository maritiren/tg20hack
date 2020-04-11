#!/usr/bin/env python3
from cryptography.fernet import Fernet
from binascii import unhexlify
from base64 import b64encode
import requests


def get(path, data=None):
    return requests.get(f"http://localhost:5000/{path}", data=data)


def decrypt(cipher, key):
    return Fernet(key).decrypt(cipher)


def main():
    pubkey = "39a32a9b03510e26eb1e06158e2408de661005da4c6e2d770cb51b725b7a417c427cbf07f4def9211b1f7e749eb76df51bce5cff422f80aa1a4e9e490ab1bc64bb33cc5c4b1568c0119fdabc3ed82743fe93e72018b3df62857370640ad15bc2aa5d1b5effcb752894658a3da9731506bedaae7566676626199c17d2a34329d29189b4b1998994690a7e913da20ba0fb381abfd8e5f601e461d8021cf472146091f87580e1469cfbf4a4ae21ad2dd85293cbf15d6ee26e9f69c261e38784c0fdfd699dbe7a8aff3a7cd9b5270382baa16d62bca5deb8b487a88d45d4c165750ab72a7b3f3069948f890cfd6396afa6bc738c4659b5e8197981f519bb74ec31486050a9d2256af6c68117aacdca4a09ce15890c98726b675cc4c3682dd6723cf80bc7d1f075b1d8561bdc8f4e6c0fa4efdc03ffc1b8b6d2cb93269c67f202150804a14f3b8a4e874ddbc781fc15bf388922b717ba3ad84dfdb08f19bd3c069c53be820c7793e65886483d64c00f0a075d829f412ed0fb0ae344c63f06717c12c86fa0b1b63c735543e60e10a5a11a92ec6793343e870658179ac51b33af72b8801f8ca4a298d68a00893e728d4147949dedae5b9059391cae918999c5c11aa64321e8e71f42d1477cd7609c9a7b443f438a1abbd1368f1336e8435f107377054a17c00b95c08c979441d3373fe35b4faad2e0cafca14429f1eeceb9f1fd6a96841070215dd5bb8fbeb3e3dd0f1e182755c1024a012627f589d9cf2ddcdd21cb24a371e8e376be38de89b3a301c313ac769c5bc9d0f1bb4586b01b3f85b19cb2e94f700fc4aa81ba5ab776cf7257d5e5c0683f960721dfa93d0cc723bdea4bcf6dba1fadd806725760665c1fa5350c4248335c4a9ebbf466b8968381783397172a93b3d0a9cc9eaf99c94c65264730a379827e3c2f16abe44ad9336bc2a94aeb29cb1859986da119affd2ffa81c07300c1dec3b4dad1db6639469219aa2278d1499e163d16e8d868e94c3b2cb5e7a32a15d663b6da824e9d247ec8dbda83a13baa2374abe3453eb1680261a01d86e0bddb1b8c221cd86c9ca033ddf290d87f13e2554bd659713b1f5718f1948d3fbfc6ecd64fac54187b94421bcea82b3cd496c35e1f8d134cc8e3b94ebae6de57f4e2be82d02dac7d08c06a17ad2e6a413c8f45559f75105e11bad7ed8eb1a2a7ad5a496fabde18062d301a4bf9c982d46614d22865b9c2523aec99660221e11fc663e9ebf675fd3abb9178afbd503045dc25b35ea36eaf725f33c788e685aea601164f9504007748501fb0f6b87e5bfb5d13f58c34467164938fd3e02401399107bcae4d09174cbde7af027af36f45f487be64da63b816dec2529e8e374de55bc05d4e0616334fa6531070ae86b49d09a68eeaf1625863069f1cd7e648b786d0c9ad05722d81abd2c6e9b2f88c8ec54de108c4ec10d09d3ba865854fdd4b1abddddcf82710de314bf60d82be4a16a2e8a95d463a77e2276cd9dd5ef9c76c72062e6ecb072ab6808cc7f3be39f1262d7cbff5654261951e9a9e3f6bebcbf33ca19ad48a3c874448d3fceb5f13c624fec4d5aaf4c5721a048e207efb87292767a634b2a2761e5d28bffdb082f42a76895675bfe81dd9feeb307a788e0abecfd932820685939cc4ec8031e6ab181e4634f168bd249ca64a69624739fb6770a0595e37bcb2c76ae080afad2043b2cfc72fc86519ae709b692853a52e52ff826aecd79aaf9f3c238ee324935509f6589d42e53f3b4504b1c2b79a34bc47e1361b544f6516e084861210f67a31eccea80aa09223a977c5f988231d8453dec962ba43301c252143b8f31ee7607fe1a092b1f8f828bf54998c4c6e3f498330248eb0e28501e701ec8b589f61a95721d3d54d6415dfb3a1c20f7be6d0f28d052c2f41dd8e3d18f50f7568d53b8524c19e6070c0d517ff8db10012d3f2b72aa5145e43e5457e5c32be84a105cabdd9bb49067f5f11478d08e31f1ffd53a6ce9e2739696b5eace42d42425d046aeb5bf9b95753e426ec5840227d5018f101fb09915cd7db92964c41a37da82af717cfb77043e35468cee61f72b935576ea69ac07a67d0f11b3f8cc116f1d94270ca08db154f0d2b5a5865e5138f16fd46f7203bb5d961e1d106a2b2b3a428c7bef666c8210806e76915f40ffe65c18e9b0f765a49934ae0efc256535ba9ca02f7cc7346d100cf47433ffa4f8b18aab4ab32a6b80cfabb1fccbdf5d99c4bd4e4f2a787f634f9d26a7138d773df2b618c575c20f57140c53fa6b9ca662758b8867eef743878a434c2a07060b95e265a079519388c9f14d1688a9963390c4c0cddca625356544f8c10b9f80e169003726b70ae53f058bb0246a4dfa7b4710788f8e098a337f540bfb503b3192efa656c452d0c15c167935821acb8e8157c1ee6f7c560ea721aee444630df2a6bea8f88e533df5a8d3c0bfe21013598504761fc9e8ddbe66184b281810673e9236b3ad5b4af2ba7d1ebe477c81441f86728cd6e1a0b2a3286928089d6597f8add71e10cb60b2ea668c66e7108562420a36a3fb23e4728421725474e7c2aed6da2bf2565e59f4793aaacf36e0e52ff5656b66039867da0be6ae1fa944ca90a5d699e80631d4a9ae75bc78d28008a6bb0a66dd02e681723f18a11649c38c819ebccecf41590161263b77983d35193f6e7fcfe2f561291463653ad851ec1fe578965a3952c964655239e2c61768cdad5b2028eabaeb6c05b629fe5893ef00e49afceb2ae3de4cbfa7e6082f93b15c45f7a5bf13e8240f3ad13d032bc9b865d20e3078b82baa111306eba143da50fa7682bf3b7dc9fdab4fd4a42d8b83181ce811ea324576c9b2ae1710905bd3f78597df96dcb4eb0c2a95cf327d01a2f0931b6f684fffbea4bb230135bba40122f8c402d53d143d4021461c5338d1b100090290af7d2e07e3a0360c0d3bce03ba3795b4c563b5c790a1ca4ee3d394df49e6a8724cba9357e71c6b54cd28607df75b15511b7ea5e978d94d09d489fd7da8b142b17af50e90d37d3575fbd0ec4168f8fe00d33978d142bb035bf821a0a2ea0a8ba2e13a501fee712a830a5a6705bfc05c41af026b5d2d2ed3a7f9a4c36493439a47a97eb243e30880170e2143bf9756d326febbdcaf01ad7fb4e7df95b65dc0a4c9276945d2a5ba7ea2b6762c2cf2ca4570fa795268c25f33892838d0816e6f74a0efa5abae038b3636f2c1dc109ed828e03c7a10872d74564a8cb3bb618ee390d3635367cdfe39b31c0e9a0a8dafbb5a3b54e0758327256c0c17f435a13cb15edd0fd003b3a5472eddee7dcaf5f8c57bff25a07c6808229b15ef772b01abe46e18e93822a29d215ba14edb4752f2235af4976710897866a9418a4a70639f52086afa1e1e1472be4bb9a91812de3e6d25de652e76bc130125222d7bd48f42e3b9d89c5b2b94f5fda50a72c3156e869702888dfaba27db0ef41fe96d412a791dfdd3e05ae2a3273baa2da14647276405671c759ad43290536b85e17ea087b69333928edf681b7ad3f3507992beb99dd6d3a35e53db2410adce476e4898898b919478785a4620739314e4c020805410a2017b1dde7274fef09462549cd2a4575eb754d561b5d30d8162d76aa0a65f8de8916cb3f"
    cipher = "ca669bb04a1c37e00be181d121b5863f418e15666341fe64d067f8c2b935a98347b7bdb590534c9ff4aeced669ac70f23f21265988eccf061725e428b28d5f7794a368991912d1f21567289bca56c0c9decf0880f6f0074758ba1c2cdfdb4ef0003cc7fdccf2a44e5d033c54b444f51e63d4c7db7838114739fef8a921da85153dd1980fdd4f5a6a7a6fe9df5e5a1ca74e57db43e17c0489620e7acb575c6d62904776c3138b3f0888a9f784aa82beae7abecd749717944fb2ffbe7fa70e63a2c2bd120cfd9883df24e8cf2826654fde822362c2727f340fdb73d5b2a45eee435a2bc7703a6aab5bf57303473f16a0d5b84f0bba5ae6d661bf43f2e61531952f9e470ac45012df794fc2511db2206cb80178a546d65c6f9cbdd6cabf10bb4cf8cfd19a3307a4c6d91ebca20b7c7600cfcc9dd87ffd8fd6100f58f285882e3b3a8beff80dbf4d5ca93255d68a9770ed77cc2ff274cbad754e10da5db5dc4b2c80fc61dfbde8956f8b0a2a2a3b5c0133c92e82bd862593fce2d30b30d711e6edbb5c63451bc0f1d470f8837532a800d7ba0159e7c3eba5fb6dbdab04ab2d33c8d2b326d28fb8ff276e6ba3ccddd36da99da76cbf48460eac91d369181e14316f2987d5ff952d5c82d37aaee199c65d4d7aa4a2147f31e7c7a2cf7cbe23af419f7ae3ad2530efe9d7c06173c5cb509ca4df6c785e4cc6516b9248626abebc92b767e433feb1a73cb0bdcdd7a3dd541973897fc60eb823d6d2392c5da1c9724a9e07f1a0c85fb3837618c40a351136048cb7b0eb89ca96e5b327ebc26501129084ef7d703a863a5ac407944bbe58f2384eeb0f549e2e3dd89f15c103202194dc0900f7342720424b0d0c24e34d9f46647294ad0487883a166f3179372cc36f2774dd8012d199c858f7217ce0179105f5e2d0f7b9c58adfff685c516a4cfc108cb750ff288801e0286a3aa8b1b394e5e8c1a2f2d15425ace651b3b8c588c935ba8ab3302197573edff440056ce20f91098d14dfd3612aac13f384bdcccda48598a62732bf04dbb8bac9d112b107d5fb1da60d36cf3fd76eddb8eb1746e84733f3198e50e0494fa04651a910030bf037fb7fc67ccb1cdd04623db018947b441269da8fcad38f8ba22ad7076acd2cb30324e4f630532024e236c97e602b88d0a9fa14c67cad70d289a66815a52c6982a4d43586b219e0a7349ebcda4325e2cb64e9e0c5d38b462c55abb6cacbe44f6918eef8ee7b88fe81cea58fdfbebb8ac447e6ee925281084bbbfe75bac89c9c609da0b28fae664de3acf5e438b6818bc7f684585bee96b41cd53755de51789de11650a0ec5a0afcb796b83739a077012cb9ecdfae60aaa5ea8cb86bcd0b51238cbb15416a6ba0830a7d7736213bb49e2f37ec06e4e661aff2a1e4aef5008c5b324d544a2486d8fb2f02a0da8390b75a1597b3c3296c090d5bea99fad71b979359b7d17edf41ae892af938b86e6cdaebfe4da414bde0fa387ba9ea822ce8d454eea0b8cf75e433b63a0751fe57b8094e4fa3e79de36b4be6c247784fac49497b3a1f7a37711d8d43367d4511980ca56f3d43757e9c30ecb31e738c1e6f35a38044c01f400ca675bc67f5b074cf5ebf462eaa20be55daeb45804e200d6ca658812f792325548a330c0638020b1a363d3dcba49ea3403d481c3235a48d1f514a482ddcd9a2a59df576c8d51288c1a4fe8478edbf3865f05d7b55a33648bb1736940f383bc9c126b1da75a52f3c42050fa957933554f68d229430318fa8f8c248a729ba8f02db88840d82645f02c5484d23c6ca8269b449a6b7831447afa236ac26e9571d9998b65bd09a5e48f0c2cdf091fc266286892d5760a729cdd77522dcdfa59a96a8b9937b19b6018b415a9f2d9f37d8d0a00e8145fc47ae5af74033eba63c65d9f2e3776ec803fb27726e626d4ebecd4d721876493f8aadcdc2cab230cf9b00be8d464ff4867ebab50e9419868f83c9301be53bdb838d15c20c939a90c205df2f2cee9d15dd00544764811ac79100abad69949ab57794b9b50ed8d301a71b5ceeffd318896e782ca4438209942b2f14f41ace7021adb4d1f4b0a20aa48c2c5ffe42c6c78f3c89d0152cd8f2e4e60e1361ad753a94e45e06894a5e2bbe73b30e49e13c312de3199f6459819a5cbbf906119c3b6953ae00ce36b8bab3c78b0720840748c2ad9ec10e9a23d2de3c8461029c132a1c8aa191ffe13ffd835dc2250a29b8c7b58740f3ed37f3aa05d3c6aa8af43e600c4cde9429cad54c250ecacd9598c00b93cbf5c4a23fbd0bdf9790b1f10459b27aa7836d2cc022dfe71c0a0219e0788343bba997ca1fbe61fd40148c4d6fc4de2c6580ca7ff18b8c1b9e8c2beacba8b884075ba5d3bc58ae58105eaac4b1230848d4e9ce43ec93ff0b8346c6d8f43a40b7a2d6f4f77e388cd6b8d5044543ac6910286992800fda7e88075ce413cd54610a650b0a7c972a6e7b0e04973959f134e437b7f1ae670bcbbcb9de3e79b47a63b135c68bb798111fc8f275c46af6ad94b5b9486e13e3a8fb043e137c70a4fee04e557f3a16daf399de17455211dadbce043b7f35b5609b370642f1732868771006dde5000278f70236e5702d04104b4b2f946f03f5065d962cd87beb04853a552eda146037f3b6aeba488f4210d6e7d9b7a14ddaf357278da4017cd73e26d2519d92da7d34c4b16b93e8466bd28a4781b7fc62565b3cf103fc9d22acc617bd10556321195455245744a67bda6700f95b6ff60b68cb250ae8bad4b38e84139789f448dcff112067d0b3e2413065a4c03371002478d9f930f21d377f53dbcb754761c59010d07fc6e5ba4d88adc31fe5a588ef05f00cbb3a0187ab98f881d4c619c0811ad0df477a5fdbbf1df9f498a152edc2b10c1382298bc18ff57d353751c519fe49c6a6b2e4ced5d54868e925cb7a3c1daf1952176f0df015d2cfe64e6dc1434fb74071f754000c3c05bf0d820bc7c27e324e5af4729924fbdd7232383998e43dab7bb2ca3277b97ee10c64ac407652dab46069776e3dc3ffe4a0794a8404523d1151ce1ea6a4a4456fbed27136f78e947d7f94ada3408d7c0a3452b2ab1e15b9da9ea2281f168b0b59f11919a78acc9ca502ef374091d9bd91ee3bcb4c09c923c97cda3646ab7e6d17997bb3335b5c86804d8f42c694735d995a44f18315b431f3d87fdf0f9a7d5434363b22fa58a306b349fa505c0ec81ac253c78b48d7d9205e5dc36ad37171527fa3e9c98a60b83a332779c4eba32d47ff89a0197aa8ec7b88a481cdb83f818a6303cebc3ac5"
    assert(get("key").text == pubkey)
    enc_flag = get("flag", data=cipher)
    secret = b64encode(unhexlify("6120918c610646d003d64692237e0da87786e188ac3d4a803b50ec1d3efe076c"))
    print(decrypt(enc_flag.text.encode(), secret).decode())


if __name__ == "__main__":
    main()
